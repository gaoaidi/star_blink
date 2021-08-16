fclock = pygame.time.Clock()   * creat a object to track time(控制时间) *
fps = 40
fclock.tick(fps)  * 控制每次屏幕刷新的时间间隔，每次屏幕刷新后都引用此方法 （This method should be called once per frame. It will compute how many milliseconds have passed since the previous call.）*

