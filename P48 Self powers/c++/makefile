#Simpliest C++ makefile in existance

TARGET = p48
CC = g++

CFLAGS  = -g -Wall


all: $(TARGET)

$(TARGET): $(TARGET).cpp
	$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).cpp

clean:
	$(RM) $(TARGET)