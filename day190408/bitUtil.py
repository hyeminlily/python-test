import pandas as pd

def getMovies():
    # scores = pd.read_csv("Data/scores.csv")
    # print(type(scores))     → <class 'pandas.core.frame.DataFrame'>

    # help(pd.read_csv)
    # read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal=b'.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=None, error_bad_lines=True, warn_bad_lines=True, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)

    # help((pd.merge))
    # merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)

    movies = pd.read_csv("Data/movies.dat", sep='::', header=None, names=['movieid', 'title', 'genre'], engine='python')
    users = pd.read_csv("Data/users.dat", sep='::', header=None, names=['userid', 'gender', 'age', 'job', 'zipcode'], engine='python')
    ratings = pd.read_csv("Data/ratings.dat", sep='::', header=None, names=['userid', 'movieid', 'rating', 'timestamp'], engine='python')

    df = pd.merge(pd.merge(movies, ratings), users)
    return df

def get_500_movie():
    df = getMovies()
    count = df.pivot_table(values='rating', index='title', aggfunc='count')

    # 평가 건수가 500개 이상인 영화 제목을 출력
    # print(count['rating'] >= 500)     # boolean 값을 반환

    title_500 = count[count['rating'] >= 500]
    # print(title_500)

    # 내림차순 정렬
    title_500_sort = title_500.sort_values(by='rating', ascending=False)
    print(title_500_sort)

    return title_500_sort

