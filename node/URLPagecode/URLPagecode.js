const http = require('http');

const server = http.createServer((req, res) => {
    res.setHeader('Conten-Type', 'text/html; charset=utf-8');
    if(req.url === '/'){
        res.statusCode = 200;
        res.end('<h1>안녕하세요! 이곳은 나의 첫 Node.js 웹 서버입니다.</h1>');
    }
    else if(req.url === '/about'){
        res.statusCode = 200;
        res.end('<h1>소개 페이지</h1>');
    }
    else{
        res.statusCode = 404;
        res.end('<h1>404 페이지를 찾을 수 없습니다.</h1>');
    }
});

const PORT = 3000;
server.listen(PORT, ()=>{
    console.log('서버가 실행 중입니다! http://localhost:${PORT} 으로 접속해 보세요.');
});