#define PIN_LED1 12
#define PIN_LED2 13
#define PIN_LED3 15
#define PIN_LIGHT_A0 A0

#define FASTLED_ESP8266_RAW_PIN_ORDER
#include <FastLED.h>
#define NUM_LEDS_IN_STRIPLINE 8
#define DATA_PIN 16
CRGB ledsLine[NUM_LEDS_IN_STRIPLINE];

#include <SFE_BMP180.h>
#include <Wire.h>
SFE_BMP180 pressure;
double baseline; // baseline pressure

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>
/* Assign a unique ID to this sensor at the same time */
Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);

#include <Wire.h>
#include <SparkFun_APDS9960.h>
// Global Variables
SparkFun_APDS9960 apds = SparkFun_APDS9960();
uint16_t ambient_light = 0;
uint16_t red_light = 0;
uint16_t green_light = 0;
uint16_t blue_light = 0;


char webPageMain[] PROGMEM = R"=====(
<safasf>
</asfasf>
)=====";

void setup() {
  Serial.begin(115200);
  while (!Serial);
  Serial.println("Begin scanning\n");

  Serial.println(webPageMain);
  
  LedCheck();
  LightCheck();
  StripLineCheck();
  PresureSensorCheck();
  AxelerometerCheck();
  GuesturesSensorCheck();
}

void loop() {
//  LedCheck();
//  Tumbler();
//delay(2000);
//  Serial.println("\nLoop");
}
void LedCheck()
{
  pinMode(PIN_LED1, OUTPUT);
  pinMode(PIN_LED2, OUTPUT);
  pinMode(PIN_LED3, OUTPUT);
 // pinMode(PIN_LED4, OUTPUT);
 int decay1 = 500;
  delay(decay1);
  Serial.println("\nПРОГРАММА ТЕСТИРОВАНИЯ МАКЕТА - ПО КУРСУ ПРОЕКТИРОВАНИЕ ВСТРОЕННЫХ ПРИЛОЖЕНИЙ");

  Serial.println("\n1.ПРОВЕРКА СВЕТОДИОДОВ");
  digitalWrite(PIN_LED1, 1);
  Serial.println("СИНИЙ - ON");
  delay(decay1);
  digitalWrite(PIN_LED1, 0);
  digitalWrite(PIN_LED2, 1);
 // Serial.println("LED1 - OFF");
  Serial.println("ЗЕЛЕНЫЙ - ON");
  delay(decay1);
  digitalWrite(PIN_LED2, 0);
  digitalWrite(PIN_LED3, 1);
//  Serial.println("LED2 - OFF");
  Serial.println("ЖЕЛТЫЙ - ON");
  delay(decay1);
  digitalWrite(PIN_LED3, 0);
//  digitalWrite(PIN_LED4, 1);
//  Serial.println("LED3 - OFF");
  Serial.println("ЕСЛИ СВЕТОДИОДЫ ЗАГОРЕЛИСЬ ПО ОЧЕРЕДИ - ПОДКЛЮЧЕНИЕ ПРАВИЛЬНОЕ\n");
  delay(decay1);
//  digitalWrite(PIN_LED4, 0);
//  Serial.println("LED3 - OFF");
}
void  LightCheck()
{
      Serial.println("\n2.ПРОВЕРКА ДАТЧИКА ОСВЕЩЕННОСТИ");
      int val = analogRead(PIN_LIGHT_A0);
      if(val != 0 && val != 1023)
      {
        Serial.print("ЕСЛИ ЗНАЧЕНИЕ НАХОДИТСЯ В ПРЕДЕЛАХ 0..1023, ДАТЧИК РАБОТАЕТ ПРАВИЛЬНО = ");
        Serial.println(val);
      }
      else
        Serial.println("ДАТЧИК ОСВЕЩЕННОСТИ НЕ РАБОТАЕТ\nПРОВЕРЬТЕ ПОДКЛЮЧЕНИЕ\n");
        delay(3000);
}
void  StripLineCheck()
{
  Serial.println("\n3.ПРОВЕРКА ЛИНЕЙКИ СВЕТОДИОДОВ");
  FastLED.addLeds<WS2812B, DATA_PIN, RGB>(ledsLine, NUM_LEDS_IN_STRIPLINE);
  int decay = 50;

  for(int i = 0; i < NUM_LEDS_IN_STRIPLINE; i++)
  {
    ledsLine[i] = CRGB::Red;
    FastLED.show();
    delay(decay);
    //ledsLineNow turn the LED off, then pause
    ledsLine[i] = CRGB::Black;
    FastLED.show();
    delay(decay);

    ledsLine[i] = CRGB::DarkViolet ;
    FastLED.show();
    delay(decay);
    // Now turn the LED off, then pause
    ledsLine[i] = CRGB::Black;
    FastLED.show();
    delay(decay);
 
    ledsLine[i] = CRGB::NavajoWhite;
    FastLED.show();
    delay(decay);
    // Now turn the LED off, then pause
    ledsLine[i] = CRGB::Black;
    FastLED.show();
    delay(decay);
    
    ledsLine[i] = CRGB::Salmon;
    FastLED.show();
    delay(decay);
    // Now turn the LED off, then pause
    ledsLine[i] = CRGB::Black;
    FastLED.show();
    delay(decay);
  }

  Serial.println("\nЕСЛИ СВЕТОДИОДЫ МИГАЮТ РАЗНЫМИ ЦВЕТАМИ: OK");
  Serial.println("ЕСЛИ СВЕТОДИОДЫ НЕ МИГАЮТ: ОШИБКА\n");
  delay(1000);
}

double getPressure()
{
  char status;
  double T,P,p0,a;

  // You must first get a temperature measurement to perform a pressure reading.
  
  // Start a temperature measurement:
  // If request is successful, the number of ms to wait is returned.
  // If request is unsuccessful, 0 is returned.

  status = pressure.startTemperature();
  if (status != 0)
  {
    // Wait for the measurement to complete:

    delay(status);

    // Retrieve the completed temperature measurement:
    // Note that the measurement is stored in the variable T.
    // Use '&T' to provide the address of T to the function.
    // Function returns 1 if successful, 0 if failure.

    status = pressure.getTemperature(T);
    if (status != 0)
    {
      // Start a pressure measurement:
      // The parameter is the oversampling setting, from 0 to 3 (highest res, longest wait).
      // If request is successful, the number of ms to wait is returned.
      // If request is unsuccessful, 0 is returned.

      status = pressure.startPressure(3);
      if (status != 0)
      {
        // Wait for the measurement to complete:
        delay(status);

        // Retrieve the completed pressure measurement:
        // Note that the measurement is stored in the variable P.
        // Use '&P' to provide the address of P.
        // Note also that the function requires the previous temperature measurement (T).
        // (If temperature is stable, you can do one temperature measurement for a number of pressure measurements.)
        // Function returns 1 if successful, 0 if failure.

        status = pressure.getPressure(P,T);
        if (status != 0)
        {
          return(P);
        }
        else Serial.println("error retrieving pressure measurement\n");
      }
      else Serial.println("error starting pressure measurement\n");
    }
    else Serial.println("error retrieving temperature measurement\n");
  }
  else Serial.println("error starting temperature measurement\n");
}

void PresureSensorCheck()
{

double T;
char status;
pressure.begin();
delay(30);
  if (pressure.begin())
    Serial.println("4.ДАТЧИК ДАВЛЕНИЯ - HW-596 (BMP180)");
  else
  {
    // Oops, something went wrong, this is usually a connection problem,
    // see the comments at the top of this sketch for the proper connections.

    Serial.println("BMP180 - ОШИБКА (НЕ ПОДКЛЮЧЕН?)\n\n");
    while(1); // Pause forever.
  }
  // Get the baseline pressure:
  
  baseline = getPressure();
  
  Serial.print("ДАВЛЕНИЕ: ");
  Serial.print(baseline);
  Serial.println(" мбар");
  Serial.print("ДАВЛЕНИЕ: ");
  Serial.print(baseline*0.750062);
  Serial.println(" мм.рт.ст.");
  Serial.println("ЕСЛИ ЦИФРЫ БЛИЗКИ К АТМОСФЕРНОМУ ДАВЛЕНИЮ: OK");
  Serial.println("ЕСЛИ НОЛЬ: ОШИБКА, ПРОВЕРИТЬ ПОДКЛЮЧЕНИЕ\n\n");
/*
  status = pressure.getTemperature(T);
  delay(status);
    if (status != 0)
    {
      // Print out the measurement:
      Serial.print("ТЕМПЕРАТУРА: ");
      Serial.print(T,1);
      Serial.print(" град\n\n");
      
    }
*/  
}
void AxelerometerCheck()
{
  Serial.println("5.АКСЕЛЕРОМЕТР - ADXL345");
    /* Initialise the sensor */
  if(!accel.begin())
  {
    /* There was a problem detecting the ADXL345 ... check your connections */
    Serial.println("ADXL345 НЕ ДЕТЕКТИРУЕТСЯ. ПРОВЕРИТЬ СОЕДИНЕНИЕ.");
    while(1);
  }

  /* Set the range to whatever is appropriate for your project */
  accel.setRange(ADXL345_RANGE_16_G);
  // accel.setRange(ADXL345_RANGE_8_G);
  // accel.setRange(ADXL345_RANGE_4_G);
  // accel.setRange(ADXL345_RANGE_2_G);

  int i = 0;
  /* Display the results (acceleration is measured in m/s^2) */
  while(i++ < 10)
  {
  /* Get a new sensor event */ 
  sensors_event_t event; 
  accel.getEvent(&event);

    Serial.print("X: "); Serial.print(event.acceleration.x); Serial.print("  ");
    Serial.print("Y: "); Serial.print(event.acceleration.y); Serial.print("  ");
    Serial.print("Z: "); Serial.print(event.acceleration.z); Serial.print("  ");Serial.println("m/s^2 ");
    delay(300);
  }
    
  Serial.println("ЕСЛИ ПРИСУТСТВУЮТ РАЗНЫЕ ЗНАЧЕНИЯ БЛИЗКИЕ к 9.6: OK");
  Serial.println("ЕСЛИ НЕТ ЗНАЧЕНИЙ, ОШИБКА. НУЖНО ПРОВЕРИТЬ ПОДКЛЮЧЕНИЕ\n");
}
void GuesturesSensorCheck()
{
  Serial.println(F("6.ДАТЧИК ЖЕСТОВ, ЦВЕТА, ПРИБЛИЖЕНИЯ И ОСВЕЩЕННОСИ APDS-9960"));
//  Serial.println(F("SparkFun APDS-9960 - ColorSensor"));
  // Initialize APDS-9960 (configure I2C and initial values)
  if ( apds.init() ) {
    Serial.println(F("APDS-9960 initialization complete"));
  } else {
    Serial.println(F("Something went wrong during APDS-9960 init!"));
  }
  // Start running the APDS-9960 light sensor (no interrupts)
  if ( apds.enableLightSensor(false) ) {
    Serial.println(F("Light sensor is now running"));
  } else {
    Serial.println(F("Something went wrong during light sensor init!"));
  }
  // Wait for initialization and calibration to finish
  delay(300);

  int i = 0;
  while(i++ < 10)
  {
    // Read the light levels (ambient, red, green, blue)
    if (  !apds.readAmbientLight(ambient_light) ||
          !apds.readRedLight(red_light) ||
          !apds.readGreenLight(green_light) ||
          !apds.readBlueLight(blue_light) ) {
      Serial.println("ОШИБКА ПРИ ЧТЕНИИ ПАРАМЕТРОВ");
    } else {
      Serial.print("Ambient: ");
      Serial.print(ambient_light);
      Serial.print(" Red: ");
      Serial.print(red_light);
      Serial.print(" Green: ");
      Serial.print(green_light);
      Serial.print(" Blue: ");
      Serial.println(blue_light);
    }
    
    // Wait 1 second before next reading
    delay(300);
  }
  Serial.println(F("\nЕСЛИ ПРИСУТСТВУЮТ РАЗНЫЕ ЗНАЧЕНИЯ ЦВЕТОВ: OK"));
  Serial.print("\n\n\n ТЕСТИРОВАНИЕ ЗАВЕРШЕНО");
}
void Tumbler(){
}
