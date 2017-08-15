const assert =  require('assert');

describe('#hello.js', () => {
    before(() => {
        console.log('hello, before');
    });
    describe('iner', () => {
        before(function () {
            console.log('before.');
        });
        
        after(function () {
            console.log('after.');
        });
        
        it('1-', () => {
            assert.strictEqual(0, 0);
        });
        beforeEach(function () {
            console.log('iner.beforeEach');
        });
        afterEach(function () {
            console.log('iner.afterEach');
        });
    });
    describe('ouer', () => {
        it('-2-', () => {
            assert.strictEqual(1, 1);
        });
    });
});