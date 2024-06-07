import mlx.core as mx
from mlx_vlm import load, generate

model_path = "mlx-community/llava-phi-3-mini-4bit"
model, processor = load(model_path)

prompt = processor.tokenizer.apply_chat_template(
    [{"role": "user", "content": f"<image>\nWhat are these?"}],
    tokenize=False,
    add_generation_prompt=True,
)

output = generate(model, processor, "images/ffc84201-3e55-5666-ad43-6c25fdf03714_323.46_1.jpg", prompt)
print(output)