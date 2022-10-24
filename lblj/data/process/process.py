import jsonlines


def jsonl_process(src_name, des_name):
    with jsonlines.open(des_name, mode="a") as writer:
        with open(src_name, "r+", encoding="utf-8") as f:
            for item in jsonlines.Reader(f):
                writer.write(item)


if __name__ == '__main__':
    # train_text.jsonl
    jsonl_process("../stage_1/train_text.jsonl", "../stage_1/train_text_v1.jsonl")

    # train_entry.jsonl
    jsonl_process("../stage_1/train_entry.jsonl", "../stage_1/train_entry_v1.jsonl")
