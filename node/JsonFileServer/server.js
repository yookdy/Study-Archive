const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
    if (req.url === '/api/users') {
        // 1. 'text'가 아닌 'utf8'로 수정
        fs.readFile('./data.json', 'utf8', (err, data) => {
            if (err) {
                // 2. restatusCode 오타 수정
                res.statusCode = 500;
                res.setHeader('Content-Type', 'text/plain; charset=utf-8');
                res.end('서버 오류');
            } else {
                res.statusCode = 200;
                // 3. applicartion 오타 수정 (application)
                res.setHeader('Content-Type', 'application/json; charset=utf-8');
                res.end(data);
            }
        });
    } else {
        res.statusCode = 404; // 400 대신 404(Not Found)가 더 적합합니다.
        res.setHeader('Content-Type', 'text/plain; charset=utf-8');
        res.end('잘못된 요청입니다.');
    }
});

const PORT = 3000;
server.listen(PORT, () => {
    // 4. 변수 출력을 위해 일반 따옴표(') 대신 백틱(`) 사용
    console.log(`Json File Server is running on: http://localhost:${PORT}/api/users`);
});