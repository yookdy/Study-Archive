const http = require('http');

const server = http.createServer((req,res)=>{
    res.setHeader('content-Type', 'text/html; charset=utf-8');
    if(req.url === '/'){
        res.statusCode = 200;
        res.end('<h1>🏠 메인 홈페이지</h1><p>환영합니다! 이곳은 홈 화면입니다.</p><a href="/about">소개 페이지로 가기</a>');
    }
    else if(req.url === '/about'){
        res.statusCode = 200;
        res.end('<h1>📖 소개 페이지</h1><p>이곳은 소개 페이지입니다.</p><a href="/">홈으로 돌아가기</a>');
    }
    else if(req.url === '/api/info'){
        res,statusCode = 200;
        res.setHeader('Content-Type', 'application/json; charset=utf-8');
        const info = {version: '1.0.0', status: 'running'};
        res.end(JSON.stringify(info
        ));
    }
    else{
        res.statusCode = 404;
        res.end('<h1>404 페이지를 찾을 수 없습니다.</h1><a href="/">홈으로 돌아가기</a>');
    }
});
const PORT = 3000;
server.listen(PORT, ()=>{
    console.log('라우팅 서버 실행 중: http;//localhost:${PORT}');
})