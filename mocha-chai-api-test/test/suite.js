const assert = require('chai').expect;
const getusertFunc = require('../object/getUser')
const postcreateUser = require('../object/postCreate')
const data = require('../data/data')

describe('API User Test', function() {
    it('Should Get User by ID', async function() {
        const res = await getusertFunc.getUser(data.id)
        assert(res.status).to.equal(200)
        assert(res.body.data.id).to.equal(data.id)
        assert(res.body.data.email).to.equal(data.email)
        assert(res.body.data.first_name).to.equal(data.first_name)
        assert(res.body.data.last_name).to.equal(data.last_name)
        assert(res.body.data.avatar).to.equal(data.avatar)
    });
    it('Should Create User', async function() {
        const res = await postcreateUser.createUser(data.name,data.job)
        assert(res.status).to.equal(201)
        assert(res.body.name).to.equal(data.name)
        assert(res.body.job).to.equal(data.job)
        assert(res.body.id).to.exist
        assert(res.body.createdAt).to.exist
    });

})