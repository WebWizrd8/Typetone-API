from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData

metadata = MetaData()

urlcodetable = Table (
    "UrlCode",
    metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("url", String(), nullable = False),
    Column("shortcode", String(6), nullable = False, unique = True),
    Column("created", DateTime),
    Column("lastRedirect", DateTime),
    Column("redirectCount", Integer),
)