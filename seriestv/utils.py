def get_proper_series_data(s, ep):
	d = {}
	for each_series in s:
		for each_episode in ep:
			if each_episode.series == each_series:
				if each_series in d:
					if each_episode not in d[each_series]:
						d[each_series].append(each_episode)
				else:
					d.update({each_series: [each_episode]})
	return (d, len(d))