FROM nginx:latest

COPY default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]


# foreground <-> background
# daemon off --> foreground 로 실행하겠다드
# 도커는 무조건 포그라운드