import cv2
from transformers import (
    Qwen2VLForConditionalGeneration, 
    AutoTokenizer,
    AutoProcessor as QwenProcessor,
)
from qwen_vl_utils import process_vision_info
from PIL import Image
import torch

# Load Qwen2-VL model and processor
qwen_processor = QwenProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")
qwen_tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")
qwen_model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-7B-Instruct",
    torch_dtype=torch.float16,
    device_map="auto"
)

def process_frame_with_qwen(frame, question):
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "image": image,
                },
                {"type": "text", "text": question},
            ],
        }
    ]

    text = qwen_processor.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = qwen_processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )
    inputs = inputs.to("cuda")

    generate_inputs = {
        'input_ids': inputs['input_ids'],
        'attention_mask': inputs['attention_mask'],
        'pixel_values': inputs['pixel_values']
    }
    generate_ids = qwen_model.generate(**generate_inputs, image_grid_thw=inputs['image_grid_thw'], max_new_tokens=128)

    if isinstance(generate_ids, list):
        generate_ids_trimmed = [out_ids[len(inputs['input_ids'][0]):] for out_ids in generate_ids]
    elif isinstance(generate_ids, torch.Tensor):
        generate_ids_trimmed = generate_ids[:, len(inputs['input_ids'][0]):]
    else:
        raise ValueError("Unexpected type for generate_ids")

    output_text = qwen_processor.batch_decode(
        generate_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    return output_text
# Open the RTSP stream
rtsp_link = 0# Replace with your RTSP link
cap = cv2.VideoCapture(rtsp_link)

if not cap.isOpened():
    print("Error opening RTSP stream")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error reading frame")
        break


    # Prompt for a question
    question = input("Ask a question about the image (Qwen): ")

    output_text = process_frame_with_qwen(frame, question)
    print(output_text)
    
    cv2.imshow("OwenVision", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()