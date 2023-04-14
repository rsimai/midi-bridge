# MIDI-bridge

An attempt to use generic MIDI controllers for various control purposes. Incoming MIDI events are mapped to outgoing commands that include

* MIDI messages to target devices
* OSC capable devices such as digital mixers
* system commands, such as emulating keystrokes

## Mappings 
Mappings should be done in a human readable text configuration file, one file per device or with an easy way to merge them into one. YAML or JSON may suit.

## The program 
continuously reads from the device through the OS's MIDI system. Each expected MIDI message triggers one or more activities, depending on the type. 

## Values
For control change messages the (usually 7-bit) value is to be preserved in a variable and to be used within the activity. The mapping config should allow conversion parameters, e.g. to convert from int 0-127 into float 0-1.

## Activities examples

* send value from encoder 1 to the software synth's filter frequency
* send value from slider 9 to the digital mixer's master volume
* toggle digital mixer's channel 1 mute with note_on 20 button and toggle the button LED as well
* send value from encoder 2 to pactl -- set-sink-volume 0

## Issues

### Sliders
Sliders have a state, the target's value may jump once it is moved and sends data. Unless they are motorized there's no way to set them, probably a "catch" feature may help which trigger changes only after values matched once. This needs two activities: read and see if small difference, then send.

### Encoders
Encoders have internal counters that wouldn't initially match the target's state. This requires initialization.

### LEDs
LEDs associated with buttons or encoders wouldn't initially represent the target's state. This requires initialization. 

### Toggle state
In order to toggle one has to read the actual value first. This requires up to three activities: read state, change state, set indicator accordingly.

### Latency
Sliders that send (nearly) all values even when moving fast may create a lot of traffic and actions queue up. Skipping some may be required and justified, if superseded by following.

### Multiple devices of the same type
There is no easy way to distinguish between them as the OS assigns the port but the config needs to allow.
