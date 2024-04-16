text = {"text": "我通常会等待切达干酪版本降至 6.00 "
                "美元左右（更宽的面条），但已经过了一分钟.所以我试着用这些来支撑我。第一口（勺子/叉子/什么）就像“天哪，当他们说辣时，他们不是在开玩笑”，到最后一口..“我必须再做一次..就像现在一样“!!",
        "items": [{"confidence": 0.964121, "negative_prob": 0.983854, "positive_prob": 0.0161456, "sentiment": 0}],
        "log_id": 1780155630679556280}
items = text.get("items")
conf = items[0].get("confidence")
neg = items[0].get("negative_prob")
pos = items[0].get("positive_prob")

if conf > 0.7:
    if neg > 0.7 and pos < 0.2:
        print("negative")
    if neg < 0.2 and pos > 0.7:
        print("positive")
    if pos < 0.7 and neg < 0.7:
        print("neutral")

