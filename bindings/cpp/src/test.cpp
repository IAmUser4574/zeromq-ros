#include <boost/network/protocol/http/client.hpp>
#include <iostream>
#include <zmq.h>
#include <jansson.h>


namespace http = boost::network::http;


int
main(int argc, char *argv[]) {

    void *context = zmq_ctx_new ();
    void *responder = zmq_socket (context, ZMQ_REP);
    int rc = zmq_bind (responder, "tcp://*:5555");

    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " url" << std::endl;
        return 1;
    }

    try {
        http::client client;
        http::client::request request(argv[1]);
        http::client::response response = client.get(request);
        std::cout << body(response) << std::endl;
    }
    catch (std::exception &e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }

    return 0;
}
