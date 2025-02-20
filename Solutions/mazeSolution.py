
def main():
     pen.move(DOWN)
     drivetrain.set_drive_velocity(100, PERCENT)
     drivetrain.set_turn_velocity(100, PERCENT)

     while True:  # Infinite loop to keep restarting
        # Start the movement sequence
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        
        while not down_eye.detect(RED):  # Moves until it detects red
            if distance.get_distance(MM) > 250:
                drivetrain.drive_for(FORWARD, 250, MM)
                drivetrain.turn_for(RIGHT, 90, DEGREES)
            else:
                drivetrain.turn_for(LEFT, 90, DEGREES)
        
        # Red detected - stop and turn around
        drivetrain.stop()
        wait(1, SECONDS) 
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        

        # Navigate back while avoiding walls and checking for green
        while not down_eye.detect(GREEN):  
            if distance.get_distance(MM) > 250:
                drivetrain.drive_for(FORWARD, 250, MM)
                drivetrain.turn_for(RIGHT, 90, DEGREES)
            else:
                drivetrain.turn_for(LEFT, 90, DEGREES)
        drivetrain.stop()
        wait(1, SECONDS) 
        return



# VR threads — Do not delete
vr_thread(main)
