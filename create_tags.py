import scipy.io as sio


train_mat = "trainCharBound.mat"
test_mat = "testCharBound.mat"
train_tags = "train.tags"
test_tags = "test.tags"


def create_tags(mat_file, tags_file, data_key):
    tags_fo = open(tags_file, "w")
    data_dir = sio.loadmat(mat_file)
    gts = data_dir[data_key][0]
    for i in range(gts.shape[0]):
        image_path = gts[i][0][0]
        gt = gts[i][1][0]
        tags_fo.write("{} {}\n".format(image_path, gt))

    tags_fo.close()


# create_tags(train_mat, train_tags, "trainCharBound)
create_tags(test_mat, test_tags, "testCharBound")
