import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from transformers import TFAutoModelForCausalLM, AutoTokenizer

WORDS_TO_PREDICT = 10
# MODEL_NAME = "gpt2"
MODEL_NAME = "bert-base-uncased"

text = input("\nGive an incomplete sentence: ")
if text[-1] == " ": text = text[:-1]


tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = TFAutoModelForCausalLM.from_pretrained(MODEL_NAME)

for i in range(WORDS_TO_PREDICT):
    tokens = tokenizer.encode(text, return_tensors="tf")
    outputs = model(tokens).logits[:, -1, :].numpy()
    
    pred_id = outputs.argmax().item()
    pred_word = tokenizer.decode(pred_id)
    if pred_word == '\n': break
    elif pred_word == "." and text[-1] == ".": break

    print("\nGiven phrase:", text)
    if pred_word[0] == " ": print("Predicted Words:"+pred_word)
    else: print("Predicted Word:", pred_word)

    text += pred_word
    if i+1 != WORDS_TO_PREDICT:
        print("Sentence with {} extra words: {}".format(i+1, text))
    # else:
    #     for ele in tokens.numpy().tolist()[0]:
    #         print(ele, ":", tokenizer.decode(ele))

print("\nTotal predicted words added:", i+1)
print("Final sentence:", text)