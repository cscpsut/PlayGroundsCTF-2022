package main

func main() {
	route := initiateRoutes();

	route.Run(":3004")

}
