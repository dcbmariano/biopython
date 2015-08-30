if feature.type == "tRNA":
	color = colors.green
	feature.qualifiers['locus_tag'] = feature.qualifiers['product']
	gd_feature_set.add_feature(feature, color=color, label=True)