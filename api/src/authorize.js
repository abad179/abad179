function authorize(...allowedRoles) {
  const roles = Array.isArray(allowedRoles[0]) ? allowedRoles[0] : allowedRoles;
  return (req, res, next) => {
    const role = req && req.user ? req.user.role : undefined;
    if (roles.includes(role)) {
      next();
    } else {
      res.status(403).send('Forbidden');
    }
  };
}

module.exports = authorize;
