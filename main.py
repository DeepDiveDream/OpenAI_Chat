import os
import openai
import json

org_key = "org-TvYS0dkdRGFeOh7Br49t26FG"
api_key = "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"


def get_question():
    sentinel = ""  # ends when this string is seen
    text = input("Q: ")
    for line in '\n'.join(iter(input, sentinel)):
        text += line
    return text


def chat():
    openai.organization = org_key
    openai.api_key = api_key
    print("Enter you questions\n(for end conversation type 'X')")

    val = get_question()
    prompt = "Q: " + val + " A:"

    while val != 'X':
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.2,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        # print(response)
        variants = response['choices']

        for var in variants:
            print("A: " + var["text"])

        val = get_question()
        prompt = "Q: " + val + " A:"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chat()
    openai.ChatCompletion.create()

    # response = openai.Image.create(
    #     prompt="raptor with pistol in the hands",
    #     n=2,
    #     size="512x512"
    # )
    # image_url = response['data'][0]['url']

    # openai.organization = org_key
    # openai.api_key = api_key
    #
    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt="Decide whether a Tweet's sentiment is positive, neutral, or negative. Tweet: 'The new Batman is dumb"
    #            "movie!' Sentiment:",
    #     temperature=0.25,
    #     max_tokens=100,
    #     top_p=1,
    #     frequency_penalty=0.0,
    #     presence_penalty=0.0,
    #     stop=["\n"]
    # )
    #
    # print(response)
    #
    #
    # openai.organization = org_key
    # openai.api_key = api_key
    #
    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt="Decide whether a Tweet's sentiment is positive, neutral, or negative. Tweet: 'The new Batman awesome"
    #            "movie!' Sentiment:",
    #     temperature=0.25,
    #     max_tokens=100,
    #     top_p=1,
    #     frequency_penalty=0.0,
    #     presence_penalty=0.0,
    #     stop=["\n"]
    # )
    # print(response)


