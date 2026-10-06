import sys

# Simulation of a weather database (Easily replaceable with a live API later)
WEATHER_DATABASE = {
    "tokyo": {"temp": "18°C", "condition": "Rainy", "humidity": "80%"},
    "new york": {"temp": "22°C", "condition": "Sunny", "humidity": "45%"},
    "london": {"temp": "14°C", "condition": "Cloudy", "humidity": "75%"},
    "paris": {"temp": "16°C", "condition": "Windy", "humidity": "60%"},
    "sydney": {"temp": "25°C", "condition": "Clear", "humidity": "50%"}
}

def preprocess_input(user_input: str) -> str:
    """
    Cleans and standardizes the user input.
    FUTURE NLP INTEGRATION: Replace this with tokenization, lemmatization, 
    and stop-word removal using libraries like NLTK or spaCy.
    """
    if not user_input:
        return ""
    return user_input.strip().lower()

def extract_intent_and_entities(clean_input: str) -> tuple[str, str | None]:
    """
    Rule-based Intent Classification and Named Entity Recognition (NER).
    Maps keywords to actions and extracts the city name.
    
    FUTURE NLP INTEGRATION: Replace this manual keyword mapping with a 
    trained Intent Classifier (e.g., SVM, BERT) and an NER model.
    """
    # Define exit commands
    exit_keywords = ["exit", "quit", "bye", "goodbye", "stop"]
    if any(keyword in clean_input for keyword in exit_keywords):
        return "goodbye", None

    # Define greeting commands
    greeting_keywords = ["hi", "hello", "hey", "greetings"]
    if any(keyword in clean_input for keyword in greeting_keywords):
        return "greeting", None

    # Define help commands
    help_keywords = ["help", "options", "what can you do"]
    if any(keyword in clean_input for keyword in help_keywords):
        return "help", None

    # Define weather checking commands
    weather_keywords = ["weather", "temperature", "forecast", "temp", "rain", "sunny"]
    
    # Check if user mentioned weather directly or just named a known city
    found_city = None
    for city in WEATHER_DATABASE.keys():
        if city in clean_input:
            found_city = city
            break

    if any(keyword in clean_input for keyword in weather_keywords) or found_city:
        return "get_weather", found_city

    return "unknown", None

def fetch_weather(city: str | None) -> str:
    """
    Retrieves data from our database based on the extracted city entity.
    FUTURE INTEGRATION: Replace database lookup with a real-time HTTP 
    request to a weather API (e.g., OpenWeatherMap API).
    """
    if not city:
        return "Which city are you checking the weather for? (e.g., London, Tokyo)"
    
    # Matching data
    data = WEATHER_DATABASE.get(city)
    if data:
        return (f"The current weather in {city.title()} is {data['condition']} "
                f"with a temperature of {data['temp']} and {data['humidity']} humidity.")
    else:
        return (f"Sorry, I don't have weather data for '{city.title()}' right now. "
                f"Try searching for Tokyo, New York, London, Paris, or Sydney.")

def handle_response(intent: str, entity: str | None) -> str:
    """
    Generates a response based on the identified intent and entities.
    """
    if intent == "greeting":
        return "Hello! I am your Weather Assistant. How can I help you today?"
    
    elif intent == "help":
        return ("I can provide weather updates for select major cities. "
                "Just type something like 'What is the weather in London?' or 'Tokyo temperature'.")
    
    elif intent == "get_weather":
        return fetch_weather(entity)
    
    elif intent == "goodbye":
        print("Goodbye! Have a great day ahead.")
        sys.exit(0)
        
    else:
        return "I'm not sure I understand. Could you please rephrase or ask for 'help'?"

def main():
    """
    Main loop handling the chatbot session lifecycle.
    """
    print("====================================================")
    print("Weather Bot: Active. Type 'exit' to end the session.")
    print("====================================================")
    print("Weather Bot: Hi! Ask me about the weather in cities like New York or London.")
    
    while True:
        try:
            user_raw = input("\nYou: ")
            
            # Step 1: Input handling & normalization
            cleaned = preprocess_input(user_raw)
            if not cleaned:
                continue
            
            # Step 2: Extract meaning (Intent and Entities)
            intent, entity = extract_intent_and_entities(cleaned)
            
            # Step 3 & 4: Process logic and generate response
            response = handle_response(intent, entity)
            print(f"Weather Bot: {response}")
            
        except (KeyboardInterrupt, SystemExit):
            print("\nWeather Bot: Session closed. Goodbye!")
            break

if __name__ == "__main__":
    main()
