from .airlines import FlightPlanner
    
def main() -> None:
    planner=FlightPlanner()
    while True:
        print("\nWelcome to jikstra's algorithm")
        origin=input("Enter the origin airport code or q to quit: \n")
        origin=origin.upper()
        #check for quit or bad input
        if origin == 'Q':
            ('Qutting...')
            break
        if origin not in planner.airports:
            print("Invalid airport code")
            continue
        #fake out the user by asking before input is ready so the algorithm can run
        print("Enter the destination airport code: ")
        if origin != planner.source.code: #check if the origin is the same as the last one to avoid running the algorithm again
            planner.dijkstra(origin)
        #get the destination and print the path
        destination=input()
        destination=destination.upper()
        if destination not in planner.airports:
            print("Invalid airport code")
            continue
        
        planner.print_path(destination)



if __name__ == '__main__':
    main()


