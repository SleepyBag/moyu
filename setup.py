from setuptools import setup


setup(
	name='moyu',
	version='1.0',
	packages=['moyu'],
	install_requires=[
		'lunardate',
		'chinese_calendar',
	],
	entry_points = {
		'console_scripts': [
			'moyu = moyu.moyu:main'
		]
	}
)