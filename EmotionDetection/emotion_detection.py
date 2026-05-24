
import requests

def emotion_detector( text_to_analyze):
	url="https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
	headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
	input_json= {"raw_document": {"text": text_to_analyze} }
	output=requests.post(url,json=input_json,headers=headers)
	format_output= output.json()

	emo = format_output["emotionPredictions" ][0]["emotion"]
	angerval=emo["anger"]
	disgustval=emo["disgust"]
	fearval=emo["fear"]
	joyval=emo["joy"]
	sadnessval=emo["sadness"]
	overallemoscores= {"anger":angerval, "disgust":disgustval,"fear":fearval, "joy":joyval, "sadness":sadnessval}

	dominant=max(overallemoscores,key= overallemoscores.get)
	return{
	"anger": angerval,
	"disgust": disgustval,
	"fear": fearval,
	"joy": joyval,
	"sadness": sadnessval,
	"dominant_emotion": dominant
	}
