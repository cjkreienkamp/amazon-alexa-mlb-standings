# Amazon Alexa MLB Standings Skill  

This repository contains the code for an Alexa Skill that delivers up-to-date MLB standings and details about users' favorite baseball teams. By integrating this skill with Alexa-enabled devices, users can receive real-time updates on team rankings and performance.  

## Features  

- **Real-Time Standings**: Fetches and presents the latest MLB standings upon user request.  
- **Team-Specific Information**: Provides detailed standings and performance metrics for user-specified teams.  
- **Alexa Integration**: Designed to seamlessly integrate with Amazon Alexa devices, offering voice-activated interactions.  

## Prerequisites  

Before setting up this Alexa skill, ensure you have the following:  

- **Amazon Developer Account**: Required for deploying and testing Alexa Skills.  
- **AWS Lambda Account**: Used for hosting the skill's backend logic.  
- **Python 3.x**: The skill is developed using Python, so ensure you have an appropriate version installed.  

## Setup Instructions  

### 1. Clone the Repository  

Open a terminal and run:  

```bash
git clone https://github.com/cjkreienkamp/amazon-alexa-mlb-standings.git
cd amazon-alexa-mlb-standings
```

### 2. Install Dependencies

It is recommended to use a virtual environment to manage dependencies:

```bash
python -m venv env
source env/bin/activate  # On Windows, use 'env\Scripts\activate'
pip install -r requirements.txt
```

### 3. Configure AWS Lambda

- Zip the skill's code (excluding the env/ folder) and upload it to AWS Lambda.
- In the AWS Lambda console, set up an Alexa Skills Kit trigger.

### 4. Create the Alexa Skill

1. Navigate to the Alexa Developer Console
2. Click "Create Skill", name it appropriately, and choose Custom Model.
3. Configure the interaction model (Intents, Slots, and Sample Utterances).
4. Link the skill to the AWS Lambda function you created.

### 5. Testing the Skill

- Use the Alexa simulator in the Alexa Developer Console to test responses.
- If you own an Alexa-enabled device, enable developer testing to interact with the skill live.

## File Overview 
| File Name               | Description                                            |
|-------------------------|--------------------------------------------------------|
| README.md               | This file, providing an overview and setup guide.      |
| pr_01.py                | Core script for fetching and processing MLB standings. |
| pr_01_lambda.py         | AWS Lambda handler function for the Alexa Skill.       |
| openingday.py           | Script to retrieve MLB Opening Day schedules.          |
