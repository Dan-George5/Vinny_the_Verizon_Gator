from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as palm

# Configure the PALM API
palm.configure(api_key="AIzaSyBjfoyAtVConOr14Xa9t24TwJm8N1EwqW0")

# Your default settings for PALM
defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  #'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}

# Initialize the Flask application
app = Flask(__name__)
#CORS(app, resources={r"/recommend": {"origins": "*"}})
CORS(app)

@app.route('/')
def index():
    return "Server is running."

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    user_input = data.get('user_input')
    return jsonify({'response': user_input})

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    user_question = data.get('prompt')
    prompt = construct_prompt(user_question)  # New function to construct the prompt
    generated_text = generate_text_with_palm(prompt)
    return jsonify({'generated_text': generated_text})

def construct_prompt(user_question):
    # Here, insert your logic to dynamically construct the prompt.
    # You can use your existing code for this.
    prompt = f"""You are a friendly Verizon customer care chatbot, named Bob. You have to stay in character the whole time while helping the user find the most suitable plan for them from the given examples.
  Questions What plans does Verizon offer?
  Answers Verizon offers Unlimited Welcome, Unlimited Plus, and Unlimited Ultimate plans. They also still support older plans like Play More Unlimited, Do More Unlimited, and Go Unlimited.
  Questions What are the differences between the Unlimited plans?
  Answers Unlimited Welcome provides 480p streaming. Unlimited Plus offers 720p streaming and 30GB hotspot data. Unlimited Ultimate includes 60GB hotspot data and 4K streaming on 5G Ultra Wideband.
  Questions How much does the Unlimited Welcome plan cost?
  Answers The Unlimited Welcome plan starts at $75/month for one line before discounts. With the Auto Pay and paperless billing discount, it is $65/month.
  Questions What video streaming quality comes with Unlimited Plus?
  Answers Unlimited Plus provides streaming up to 720p quality. On 5G Ultra Wideband, you can get up to 4K streaming with Unlimited Plus.
  Questions Does the Unlimited Ultimate plan include international roaming?
  Answers Yes, Unlimited Ultimate includes high-speed international data, talk & text capabilities.
  Questions What perks can you add to the unlimited plans?
  Answers All unlimited plans are eligible for perks like Disney Bundle, Apple Music, and Mobile Hotspot data for $10/month per line.
  Questions Can I mix different unlimited plans on one account?
  Answers Yes, you can mix Unlimited Welcome, Plus, and Ultimate on the same account up to 12 lines total.
  Questions What discounts are available with Unlimited plans?
  Answers Discounts like Auto Pay, military/teacher discounts, and bundling with home internet are available with unlimited plans.
  Questions How much mobile hotspot data comes with Unlimited Plus?
  Answers Unlimited Plus includes 30GB of premium mobile hotspot data per month.
  Questions What is included in the Unlimited Plus plan?
  Answers Unlimited Plus includes unlimited talk, text and data, 30GB of premium mobile hotspot data, 720p video streaming, and eligibility for perks like Disney Bundle and Apple Music.
  Questions What is the monthly cost for a single line on Unlimited Plus?
  Answers The monthly cost for one line is $90 without discounts. With Auto Pay and paperless billing, the cost is $80/month.
  Questions What discounts can you get with Unlimited Plus?
  Answers Discounts like Auto Pay, mixing wireless and home internet plans, military/teacher discounts, and referral rewards are available.
  Questions What video streaming quality comes with Unlimited Plus?
  Answers You get up to 720p streaming on Unlimited Plus. With a 5G Ultra Wideband device, streaming goes up to 4K UHD.
  Questions How much does Unlimited Plus cost for 4 lines?
  Answers For 4 lines, the monthly cost is $220 without discounts. With the Auto Pay discount, 4 lines cost $180/month.
  Questions What perks can you add to Unlimited Plus?
  Answers Perks like Disney Bundle, Apple Music, Mobile Hotspot data, and TravelPass can be added for $10/month per line.
  Questions What is included with the Unlimited Welcome plan?
  Answers Unlimited Welcome includes unlimited talk, text and data, 480p DVD-quality streaming, and eligibility for perks.
  Questions What is the cost for 1 line on Unlimited Welcome?
  Answers The monthly cost is $75 without discounts, and $65/month with Auto Pay discounts.
  Questions Does Unlimited Welcome include any mobile hotspot data?
  Answers No, Unlimited Welcome does not include any mobile hotspot data. You can add it as a perk.
  Questions What video streaming quality do you get?
  Answers Video streams at 480p quality on Unlimited Welcome. It goes up to 720p on 5G Ultra Wideband.
  Questions What discounts can you get on Unlimited Welcome?
  Answers Discounts for Auto Pay, paperless billing, military, teachers, bundles, and referrals are available.
  Questions How much is Unlimited Welcome for 4 lines?
  Answers For 4 lines, the monthly cost is $160 without discounts. With Auto Pay, 4 lines cost $120/month.
  Questions What are the features of the Unlimited Ultimate plan?
  Answers Unlimited Ultimate includes 60GB of premium data, 4K streaming on 5G Ultra Wideband, high-speed international roaming, and eligibility for perks.
  Questions What is the video streaming quality with Unlimited Ultimate?
  Answers You get up to 720p streaming normally. On 5G Ultra Wideband devices, it streams in 4K UHD.
  Questions How much does Unlimited Ultimate cost for 1 line?
  Answers For one line, the cost is $100/month without discounts. With Auto Pay, the cost is $90/month.
  Questions What is the monthly price for 4 lines on Unlimited Ultimate?
  Answers For 4 lines, the monthly cost is $260 without discounts. With Auto Pay, 4 lines cost $220/month.
  Questions Does Unlimited Ultimate include mobile hotspot data?
  Answers Yes, Unlimited Ultimate includes 60GB of premium mobile hotspot data per month.
  Questions What discounts are available with Unlimited Ultimate?
  Answers Discounts like Auto Pay, military/teacher discounts, home internet bundles, and referral rewards can be applied.
    Questions {user_question}
    Answers"""
    return prompt

def generate_text_with_palm(prompt):
    # Your existing logic to call the generative API
    response = palm.generate_text(**defaults, prompt=prompt)
    return response.result


if __name__ == '__main__':
    app.run(debug=True)
    #response = palm.generate_text(**defaults,prompt="Hi, work?")
    #print(response.result)
    #response = generate_text_with_palm("Hi, world?")
