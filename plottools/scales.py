class LinearInflate:

    def __init__(self, thresh, scale):
        self.thresh = thresh
        self.scale = scale

    def forward(self, values):
        out = values.copy()
        out[abs(values) < self.thresh] = out[abs(values) < self.thresh] * self.scale
        out[values >= self.thresh] = out[values >= self.thresh] + self.thresh * (self.scale - 1)
        out[values <= -self.thresh] = out[values <= -self.thresh] - self.thresh * (self.scale - 1)
        return out

    def bacwards(self, values):
        out = values.copy()
        out[abs(values) < self.thresh * self.scale] = out[abs(values) < self.thresh * self.scale] / self.scale
        out[values >= self.thresh * self.scale] = out[values >= self.thresh * self.scale] - self.thresh * (self.scale - 1)
        out[values <= - self.thresh * self.scale] = out[values <= -self.thresh * self.scale] + self.thresh * (self.scale - 1)
        return out

    def get_transforms(self):
        return lambda v: self.forward(v), lambda v: self.bacwards(v)