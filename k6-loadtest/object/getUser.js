import { check, sleep, group } from "k6";
import { Counter, Rate } from "k6/metrics";
import http from "k6/http";
 
let ErrorgetUser = new Counter("errors_getUser");
const data = require('../data/data.js')

function getUser (id) {

    let params = {
        timeout: 12000,
        headers: {
            'Content-Type': 'application/json' }
    }

    let resp = http.get(data.BASE_URL+"/api/users/"+id,params);
    if (resp.status !== 200) {
        ErrorgetUser.add(1)
        console.log(resp.status+ " | " +resp.body);
    }
    check(resp, {
        "200 GET User": (resp) => resp.status == 200,
   });
    return resp;
}
 
export default getUser