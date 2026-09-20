const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    
    if (req.url === '/') {
        fs.readFile('./index.html', (err, data) => {
           if (err) {
            res.statusCode = 500;
            res.end('<h1>500 서버 오류</h1>');
           } else {
            res.statusCode = 200;
            res.end(data);
           }
        });
    } else {
        res.statusCode = 404;
        res.end('<h1>404 페이지를 찾을 수 없습니다.</h1>');
    }
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`서버가 실행 중입니다! http://localhost:${PORT} 으로 접속해 보세요.`);
});