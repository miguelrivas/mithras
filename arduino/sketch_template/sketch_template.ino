/*

First Arduino Program in awhile

*/

void setup()
{
  Serial.begin(9600);
}

void loop() //Runs Forever
{
  Serial.println("Hello, World!");
  delay(1000); //Delays 1000 ms
}
