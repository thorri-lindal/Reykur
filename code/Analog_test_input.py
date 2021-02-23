Serial.begin(9600);
}

void loop() {
  Serial.println(analogRead(A0));
  delay(2);
}

  Serial myPort;     
  int xPos = 1;         
  float inByte = 0;

  void setup () {
    size(400, 300);
    println(Serial.list());
    myPort = new Serial(this, Serial.list()[0], 9600);
    myPort.bufferUntil('\n');
  }
  void draw () {
    stroke(127, 34, 255);
    line(xPos, height, xPos, height - inByte);
    if (xPos >= width) {
      xPos = 0;
      background(0);
    } else {
      xPos++;
    }
  }
  void serialEvent (Serial myPort) {
    // get the ASCII string:
    String inString = myPort.readStringUntil('\n');

    if (inString != null) {
      inString = trim(inString);
      inByte = float(inString);
      println(inByte);
      inByte = map(inByte, 0, 1023, 0, height);
    }
  }
