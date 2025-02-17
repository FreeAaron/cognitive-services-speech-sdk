# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

# <code>
import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "5c44158ea50747dca208ecdf89456775", "eastus"
# speech_key, service_region = "YourSubscriptionKey", "eastus"
speech_config = speechsdk.SpeechConfig(
    subscription=speech_key, region=service_region)

# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
speech_config.speech_synthesis_voice_name = "en-GB-LibbyNeural"

# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Receives a text from console input.
print("Type some text that you want to speak...")
# text = input()
text = "That'd be just amazing!"

# Synthesizes the received text to speech.
# The synthesized speech is expected to be heard on the speaker with this line executed.
result = speech_synthesizer.speak_text_async(text).get()

speech_config.set_speech_synthesis_output_format(
    speechsdk.SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)
synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config, audio_config=None)

ssml_string = open("ssml.xml", "r").read()
result = synthesizer.speak_ssml_async(ssml_string).get()

# result = synthesizer.speak_text_async(
#     "The stars above are constantly changing, but usually these changes are too slow or too faint for the eye to see. Your challenge is to develop a learning tool to teach people about stellar variability and help them understand how dynamic the night sky really is!").get()
stream = speechsdk.AudioDataStream(result)
# stream.save_to_wav_file("path/to/write/file.wav")
stream.save_to_wav_file("speech.wav")


# Checks result.
# if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#     print(
#         "Speech synthesized to speaker for text [{}]".format(text))
# elif result.reason == speechsdk.ResultReason.Canceled:
#     cancellation_details = result.cancellation_details
#     print("Speech synthesis canceled: {}".format(cancellation_details.reason))
#     if cancellation_details.reason == speechsdk.CancellationReason.Error:
#         if cancellation_details.error_details:
#             print("Error details: {}".format(
#                 cancellation_details.error_details))
#     print("Did you update the subscription info?")
# </code>
