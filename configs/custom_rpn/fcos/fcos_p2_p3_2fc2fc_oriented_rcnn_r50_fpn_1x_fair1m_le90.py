_base_ = ['./fcos_p2_p3_sample2_oriented_rcnn_r50_fpn_1x_fair1m_le90.py']

model = dict(
    roi_head=dict(
        bbox_head=dict(
            type='RotatedConvFCBBoxHead',
            num_shared_convs=0,
            num_shared_fcs=0,
            num_cls_convs=0,
            num_cls_fcs=2,
            num_reg_convs=0,
            num_reg_fcs=2
        )
    )
)
