from django.urls import resolve, reverse

class TestSuiteMixin:    
    def setups(self):
        self.rsp = self.client.get(self.path)
        self.resolved = resolve(self.path)
        self.reverselu = self.client.get(reverse(self.name))

    def testRsp(self):
        self.assertEqual(self.rsp.status_code, 200)

    def testRspTemplate(self):
        self.assertTemplateUsed(self.rsp, self.template)

    def testRspText(self):
        self.assertContains(self.rsp, self.text)

    def testRev(self):
        self.assertEqual(self.reverselu.status_code, 200)

    def testRevTemplate(self):
        self.assertTemplateUsed(self.reverselu, self.template)

    def testRevText(self):
        self.assertContains(self.reverselu, self.text)

    def testRes(self):
        self.assertEqual(self.resolved.func.__name__, self.view.as_view().__name__)
