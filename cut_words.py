# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import jieba
import jieba.analyse # 导入提取关䭞词的库
# 对训练集 测试集文本都进行切词处理,对测试集数据打上主题标签
#存至文件؍
def save_file(save_path, content):
    with open(save_path, "a",encoding= 'utf-8',errors='ignore') as fp:
        fp.write(content)
# 读取文件
def read_file(file_path):
    with open(file_path, "r",encoding= 'utf-8',errors='ignore') as fp:
        content = fp.readlines()
        # print(content)
    return str(content)
# 抽取测试集的主题关键词
def extract_theme(content):
    themes = []
    tags = jieba.analyse.extract_tags(content, topK=3, withWeight=True, allowPOS=['n','ns','v','vn'],withFlag=True)
    for i in tags:
        themes.append(i[0].word)
    return str(themes)
def cast_words(origin_path, save_path, theme_tag):
    '''
    train_words_path: 原始文本路径
    train_save_path: 切词后文本路径
    :return:
    '''
    file_lists = os.listdir(origin_path) #原文档所在路径

    # print('\n'+'file_lists:')
    # print(file_lists)
    # print('\n'+'origin_path:')
    # print(origin_path)

    for dir_1 in file_lists: #找到文件夹
        file_path = origin_path + dir_1 + "/" #原始文件路径

        # print('\n' + 'dir_1:')
        # print(dir_1)
        #
        # print('\n' + 'file_path:')
        # print(file_path)

        seg_path = save_path + dir_1 + "/" #切词后文件路径

        # print('\n' + 'save_path:')
        # print(save_path)
        #
        # print('\n' + 'seg_path:')
        # print(seg_path)

        if not os.path.exists(seg_path):
            os.makedirs(seg_path)
        detail_paths = os.listdir(file_path)

        # print('\n' + 'detail_paths:')
        # print(detail_paths)

        for detail_path in detail_paths: #找到文件夹下具体文件路径
            full_path = file_path + detail_path #原始文件下每个文档路径

            # print('\n' + 'detail_path:')
            # print(detail_path)
            #
            # print('\n' + 'full_path:')
            # print(full_path)

            file_content = read_file(full_path)

            # print('\n' + 'file_content:')
            # print(file_content)

            file_content = file_content.strip() # replace("\r\n", " ")
                                                # 删除换行
            # print('\n' + 'file_content.strip():')
            # print(file_content)

            file_content = file_content.replace("\'", "")

            # print('\n' + 'file_content.replace("\'", ""):')
            # print(file_content)

            file_content = file_content.replace("\\n", "")

            # print('\n' + 'file_content.replace("\\n", ""):')
            # print(file_content)

            content_seg1 = jieba.cut(file_content) # 为文件内容分词
            content_seg2 = jieba.cut(file_content)  # 为文件内容分词
            # for tip in content_seg:
            #     print('这是关键词：' + tip)


            if theme_tag is not None:
                print("文件路径:{} ".format(theme_tag + detail_path))
                theme = extract_theme(" ".join(content_seg1)) #theme为该文章主题关键词

                # for tip in theme:
                #     print('这是关键词：' + tip)
                print("文章主题关键词:{} ".format(theme))
                save_file(theme_tag + detail_path, theme) # 将训练集文章的主题关键词存到标签存储路径

            save_file(seg_path + detail_path, " ".join(content_seg2)) # 将处理后的文件保存到分词后语料目录

if __name__ == "__main__":
    # 对训练集进行分词
    train_words_path = './train_segments/'  #./
    train_save_path = './train_words/'   #./
    cast_words(train_words_path,train_save_path,theme_tag=None)
    # 对测试集进行分词 抽取文章主题标签
    train_words_path = './test_segments/'  #
    train_save_path = './test_words/'  #
    theme_tag_path = './theme_tag/' #存放测试集文章主题标签路径  theme_tag/
    cast_words(train_words_path, train_save_path, theme_tag=theme_tag_path)
