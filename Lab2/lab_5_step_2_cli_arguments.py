import argparse
import boto3

parser = argparse.ArgumentParser(description="Provides translation between one source language and another")

parser.add_argument(
    '--text',
    dest="Text",
    type=str,
    help="The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character "
         "set, this may be fewer than 5,000 characters",
    required=True
)

parser.add_argument(
    '--source-language-code',
    dest="SourceLanguageCode",
    type=str,
    help="The language code for the language of the source text. The language must be a language supported by Amazon "
         "Translate.",
    required=True
)

parser.add_argument(
    '--target-language-code',
    dest="TargetLanguageCode",
    type=str,
    help="The language code requested for the language of the target text. The language must be a language support by "
         "Amazon Translate.",
    required=True
)

args = parser.parse_args()


def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)


def main():
    translate_text(**vars(args))


if __name__ == "__main__":
    main()
