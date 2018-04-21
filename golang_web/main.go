package main

import (
	"fmt"
	"github.com/gorilla/mux"
	"net/http"
)

// creates a new routes with handle 'hello'
func newRouter() *mux.Router {
	r := mux.NewRouter()
	r.HandleFunc("/hello", handler).Methods("GET")
	return r
}

func main() {
	r := newRouter()
	// We can then pass our router (after declaring all our routes) to this method
	// (where previously, we were leaving the secodn argument as nil)
	http.ListenAndServe(":8080", r)

}
func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World, Sudev's first website")
}
