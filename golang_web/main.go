package main

import (
	"fmt"
	"github.com/gorilla/mux"
	"net/http"
)

func main() {
	// Declare a new router
	r := mux.NewRouter()
	// This is where the router is useful, it allows us to declare methods that
	// this path will be valid for
	r.HandleFunc("/hello", handler).Methods("GET")

	// We can then pass our router (after declaring all our routes) to this method
	// (where previously, we were leaving the secodn argument as nil)
	http.ListenAndServe(":8080", r)

}
func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World, Sudev's first website")
}
