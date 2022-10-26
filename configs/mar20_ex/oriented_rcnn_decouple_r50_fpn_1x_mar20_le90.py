_base_ = ['./oriented_rcnn_r50_fpn_1x_mar20_le90.py']

model = dict(
    roi_head=dict(
        type='OrientedDecoupleHeadRoIHead',
        bbox_roi_extractor=dict(
            type='DecoupleRotatedSingleRoIExtractor',
            cls_feat='current',
            start_level=0,
            roi_layer=dict(
                type='RoIAlignRotated',
                out_size=7,
                sample_num=2,
                clockwise=True),
            out_channels=256,
            featmap_strides=[4, 8, 16, 32]),
        bbox_head=dict(
            type='RotatedDecoupleBBoxHead',
            num_cls_fcs=2
        )
    )
)
