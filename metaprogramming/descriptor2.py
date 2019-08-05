class SeriesProduct:
    title = Descriptor("title")
    cost_per_page = Descriptor("cost_per_page")
    is_waitfree = Descriptor("is_waitfree")
    author = Descriptor("author")


sp = SeriesProduct()
sp.title = "나혼자만 레벨업"
sp.author = "장경락"
sp.cost_per_page = 100
sp.is_waitfree = True

print(sp.__dict__)