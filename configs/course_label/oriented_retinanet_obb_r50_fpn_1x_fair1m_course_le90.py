_base_ = ['../oriented_retinanet/oriented_retinanet_obb_r50_fpn_1x_fair1m_le90.py']

dataset_type = 'FAIR1MCourseDataset'
data = dict(
    train=dict(
        type=dataset_type
    ),
    val=dict(
        type=dataset_type
    ),
    test=dict(
        type=dataset_type
    )
)

model = dict(
    bbox_head=dict(
        num_classes=5
    )
)

evaluation = dict(interval=1)