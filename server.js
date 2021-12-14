const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')

//express app
const app = express()

app.use(express.urlencoded({extended: false}))
app.use(bodyParser.json());

// to allow cors shiz
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
  });

const PORT = 5000
app.listen(PORT, () => console.log(`Server running on port ${PORT}`))

// app.use(bodyParser.urlencoded({ extended: true }))
app.use(cors())
// app.use(bodyParser.json())

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.get('/crawl/:param1', (req, res) =>{
    var searchInput = req.params.param1
    console.log("Crawling " + searchInput + "...")
    var spawn = require("child_process").spawn
    var process = spawn('python3', ["./crawl.py", searchInput])
    process.stdout.on('data', (data)=>{
        res.send(data.toString())
        console.log(data.toString())
    })  

})

// app.post('/post-location', (req, res) => {
//     //res.send('post-location')
//     res.header("Access-Control-Allow-Origin", "*");
//     res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
//    // locationPosted = req.body.loc
//     locationPosted = "Sulawesi Selatan"
//     console.log(locationPosted)
//     Provinsi.findOne({ "name" : locationPosted }, (err, result) => {
//         if (err) throw err

//         //if empty, result == null
//         if(result === null){
//             addProvinsi(locationPosted)
//         } else {
//             updateProvinsi(result.name, result.count)
//         }
//     })
//     //console.log(req.body)
// })
