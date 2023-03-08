docker run --attach STDOUT -e AWS_ACCESS_KEY_ID=foo -e AWS_SECRET_ACCESS_KEY=bar -e AWS_REGION=baz -p 2000:2000/udp --name xray-daemon xray-daemon -o;
