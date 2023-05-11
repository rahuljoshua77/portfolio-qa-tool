import testgetUser from "../object/getUser.js"
const data = require('../data/data.js')

export let options = {
    stages: [
      { duration: "10s", target: 100 },
    ]
  };

export default  () => {
    testgetUser(data.id)
}
