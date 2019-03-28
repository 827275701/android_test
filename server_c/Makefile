.PHONY:myhttpd tcp_server
myhttpd:myhttpd.c
	gcc $^ -o $@ -lpthread

tcp_server:tcp_server.c
	gcc $^ -o $@ -lpthread
.PHONY:clean
clean:
	rm myhttpd tcp_server
