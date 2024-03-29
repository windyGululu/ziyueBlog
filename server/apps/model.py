# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, Table
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from baseModel import baseModel

Base = declarative_base()
metadata = Base.metadata


class ZiyueArticleComment(baseModel):
    __tablename__ = 'ziyue_article_comments'

    id = Column(Integer, primary_key=True)
    from_uid = Column(Integer)
    to_uid = Column(Integer)
    conetnt = Column(VARCHAR(50))
    replay_commentid = Column(Integer)
    status = Column(TINYINT(1))
    created_time = Column(DateTime)
    updated_time = Column(DateTime)


class ZiyueArticleInfo(baseModel):
    __tablename__ = 'ziyue_article_infos'

    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR(50))
    author_id = Column(Integer)
    content = Column(LONGTEXT)
    tags = Column(VARCHAR(50))
    status = Column(TINYINT(1))
    comments_num = Column(Integer)
    likes_num = Column(Integer)
    dislikes_num = Column(Integer)
    collections_num = Column(Integer)
    created_time = Column(DateTime)
    updated_time = Column(DateTime)


class ZiyueArticleTage(baseModel):
    __tablename__ = 'ziyue_article_tages'

    id = Column(Integer, primary_key=True)
    tag_name = Column(VARCHAR(10))
    color = Column(VARCHAR(10))
    status = Column(TINYINT(1))
    created_time = Column(DateTime)
    updated_time = Column(DateTime)


class ZiyueLog(baseModel):
    __tablename__ = 'ziyue_logs'

    id = Column(Integer, primary_key=True)
    type = Column(VARCHAR(50))
    content = Column(VARCHAR(255))
    created_time = Column(DateTime)


class ZiyueSysRole(baseModel):
    __tablename__ = 'ziyue_sys_roles'

    id = Column(Integer, primary_key=True)
    role_name = Column(VARCHAR(50))
    status = Column(TINYINT(1))
    created_time = Column(DateTime)
    updated_time = Column(DateTime)


t_ziyue_sys_vips = Table(
    'ziyue_sys_vips', metadata,
    Column('id', Integer),
    Column('vip_name', VARCHAR(50)),
    Column('status', TINYINT(1))
)


class ZiyueUserCollectionCategory(baseModel):
    __tablename__ = 'ziyue_user_collection_category'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    category_id = Column(Integer)
    name = Column(VARCHAR(10))
    status = Column(TINYINT(1))
    created_time = Column(DateTime)
    update_time = Column(DateTime)


class ZiyueUserCollection(baseModel):
    __tablename__ = 'ziyue_user_collections'

    id = Column(Integer, primary_key=True)
    ariticle_id = Column(Integer)
    status = Column(TINYINT(1))
    created_time = Column(DateTime)
    updated_time = Column(DateTime)


class ZiyueUserInfo(baseModel):
    __tablename__ = 'ziyue_user_infos'

    id = Column(INTEGER(10), primary_key=True)
    user_name = Column(VARCHAR(50))
    email = Column(VARCHAR(50))
    password = Column(VARCHAR(255))
    tel = Column(VARCHAR(15))
    avatar = Column(VARCHAR(50))
    age = Column(INTEGER(10))
    gender = Column(TINYINT)
    address = Column(VARCHAR(50))
    role_id = Column(VARCHAR(50), nullable=False)
    vip_id = Column(TINYINT(1), nullable=False)
    created_time = Column(DateTime)
    updated_time = Column(DateTime)
    user_status = Column(TINYINT(1))
