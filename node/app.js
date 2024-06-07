const express = require('express')
const cors = require('cors');
const morgan = require('morgan');
const path = require('path');
const app = express();
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');

require('dotenv').config();

app.set('port', process.env.PORT2 || 8500)
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.json({ limit: '50mb' }))
app.use(express.urlencoded({ limit: '50mb', extended: true }))

app.use(morgan('dev'))
app.use(cookieParser())
app.use(express.static(path.join(__dirname, 'public')))
app.use(cors());

const PORT1 = process.env.PORT1 || 8000;
const PORT2 = process.env.PORT2 || 8500;
const FASTAPI_URL1 = process.env.FASTAPI_URL1;
const FASTAPI_URL2 = process.env.FASTAPI_URL2;
const NODE_URL1 = process.env.NODE_URL1;
const NODE_URL2 = process.env.NODE_URL2;

app.get('/', (req, res) => {
    res.render('index', {
        PORT1,
        PORT2,
        FASTAPI_URL1,
        FASTAPI_URL2,
        NODE_URL1,
        NODE_URL2
    });
});

app.get('/result', (req, res) => {
    const filename = req.query.filename;
    res.render('result', {
        filename: filename,
        NODE_URL1: NODE_URL1,
        FASTAPI_URL2: FASTAPI_URL2
    });
});

var main = require('./routes/main.js')
app.use('/', main)

app.listen(app.get('port'), () => {
    console.log("Port2: Sever Started~!!")
});

