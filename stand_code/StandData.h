#include <ArduinoJson.h>
#include <FastLED.h>

struct StandData{
  bool  LED1 = false,
        LED2 = false,
        LED3 = false;
        
  CRGB stripLedsColors[NUM_LEDS_IN_STRIPLINE];

  bool button1State,
       button2State,
       button3State;

  float  temperature,
          pressure;
          
  uint16_t ambient_light,
           red_light,
           green_light,
           blue_light;

  int lightness;

  float acceleration_x,
        acceleration_y,
        acceleration_z;
   
  String GetJSONString(void){
      StaticJsonDocument<700> jsonDocument;
      
      jsonDocument["LED1"] = LED1;
      jsonDocument["LED2"] = LED2;
      jsonDocument["LED3"] = LED3;
      
      jsonDocument["button1State"] = button1State;
      jsonDocument["button2State"] = button2State;
      jsonDocument["button3State"] = button3State;
      
      jsonDocument["temperature"] = temperature;
      jsonDocument["pressure"] = pressure;
      
      jsonDocument["ambient_light"] = ambient_light;
      jsonDocument["red_light"] = red_light;
      jsonDocument["green_light"] = green_light;
      jsonDocument["blue_light"] = blue_light;
      jsonDocument["lightness"] = lightness;
      
      jsonDocument["acceleration_x"] = acceleration_x;
      jsonDocument["acceleration_y"] = acceleration_y;
      jsonDocument["acceleration_z"] = acceleration_z;
      
      for(int i = 0; i < NUM_LEDS_IN_STRIPLINE; i++)
      {
        String nameObj = "leds" + (i+1);
        JsonObject color_r = jsonDocument.createNestedObject(nameObj);
        color_r["red"] = stripLedsColors[i].r;
        color_r["green"] = stripLedsColors[i].g;
        color_r["blue"] = stripLedsColors[i].b;
      }
    String tmp;
    serializeJsonPretty(jsonDocument, tmp);
    return tmp;
  }
};
